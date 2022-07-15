import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies
import random

connection = sqlite3.connect('users.db')
stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
cursor = connection.cursor()
result = cursor.execute(stmt)
r = result.fetchall()
if not r:
    exp = 'CREATE TABLE users (username,password)'
    connection.execute(exp)


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    un = params['username'][0] if 'username' in params else None
    pw = params['password'][0] if 'password' in params else None

    if path == '/register':
        user = cursor.execute('SELECT * FROM users WHERE username = ?', [un]).fetchall()
        if user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is taken'.format(un).encode()]
        else:
            page = '''<!DOCTYPE html>
                    <form action='/register'>
                        <h1>Register</h1>
                        Username <input type="text" name="username">
                        <br>
                        Password <input type="password" name="password"><br>
                        <br>
                        <input type="submit" value="Register"><br>
                        <hr>
                    </form>'''

            connection.execute('INSERT INTO multiply VALUES (?, ?)', [un, pw])
            connection.commit()
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)

            if not un:
                return [page.encode()]
            else:
                return [page.encode(), 'User {} has successfully registered'.format(un).encode(), '<a href="/account">Account</a>'.encode()]
            # INSERT CODE HERE. Use SQL commands to insert the new username and password into the table that was created.

    elif path == '/login' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            page = '''<!DOCTYPE html>
                        <form action="/login">
                        <h1>Login</h1>
                        Username <input type="text" name="username"><br>
                        Password <input type="password" name="password"><br>
                        <input type="submit" value="Log in">
                        </form>'''
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return [page.encode(), 'User {} successfully logged in. <a href="/account">Account</a>'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            return ['Incorrect username or password'.encode()]

    elif path == '/logout':
        headers.append(('Set-Cookie', 'session=0; expires=Thu, 01 Jan 1970 00:00:00 GMT'))
        start_response('200 OK', headers)
        return ['Logged out. <a href="/">Login</a>'.encode()]

    elif path == '/account':
        start_response('200 OK', headers)

        if 'HTTP_COOKIE' not in environ:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        if 'session' not in cookies:
            return ['Not logged in <a href="/login">Login</a>'.encode()]

        [un, pw] = cookies['session'].value.split(':')
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()

        if user:
            correct = 0
            wrong = 0

            cookies = http.cookies.SimpleCookie()
            if 'HTTP_COOKIE' in environ:
                correct = int(cookies['score'].value.split(':')[0])

                # [INSERT CODE FOR COOKIES HERE]

            page = '<!DOCTYPE html><html><head><title>Multiply with Score</title></head><body>'
            if 'factor1' in params and 'factor2' in params and 'answer' in params:
                f1 = int(params['factor1'][0])
                f2 = int(params['factor2'][0])
                answer = int(params['answer'][0])
                if f1 * f2 == answer:
                    page += '<p style="background-color: lightgreen">Correct. {} x {} = {}'.format(f1, f2, answer)
                    correct += 1
                elif f1 * f2 != answer:
                    page += '<p style="background-color: red">Wrong. {} x {} != {}'.format(f1, f2, answer)
                    wrong += 1

                # [INSERT CODE HERE. If the answer is right, show the “correct” message. If it’s wrong, show the “wrong” message.]

            elif 'reset' in params:
                correct = 0
                wrong = 0

            headers.append(('Set-Cookie', 'score={}:{}'.format(correct, wrong)))

            f1 = random.randrange(10) + 1
            f2 = random.randrange(10) + 1

            page += '<h1>What is {} x {}</h1>'.format(f1, f2)

            a1 = f1*f2
            n1 = random.randint(1, 100)
            n2 = random.randint(1, 100)
            n3 = random.randint(1, 100)

            while a1 is n1 or a1 is n2 or a1 is n3:
                n1 = random.randint(1, 100)
                n2 = random.randint(1, 100)
                n3 = random.randint(1, 100)

            # [INSERT CODE HERE. Create a list that stores f1*f2 (the right answer) and 3 other random answers]
            answer = [a1, n1, n2, n3]
            random.shuffle(answer)

            hyperlink = '<a href="/account?username={}&amp;password={}&amp;factor1={}&amp;factor2={}&amp;answer={}">{}: {}</a><br>'

            page += hyperlink.format(un, pw, f1, f2, answer[0], 'A.', answer[0])
            page += hyperlink.format(un, pw, f1, f2, answer[1], 'B.', answer[1])
            page += hyperlink.format(un, pw, f1, f2, answer[2], 'C.', answer[2])
            page += hyperlink.format(un, pw, f1, f2, answer[3], 'D.', answer[3])
            # [INSERT CODE HERE. Create the 4 answer hyperlinks here using string formatting.]

            page += '''<h2>Score</h2>
            Correct: {}<br>
            Wrong: {}<br>
            <a href="/account?reset=true">Reset</a>
            </body></html>'''.format(correct, wrong)

        if user:
            return [page.encode(), 'Logged in: {}. <a href="/logout">Logout</a>'.format(un).encode()]
        else:
            return [page.encode(), 'Not logged in. <a href="/">Login</a>'.encode()]

    elif path == '/':
        user = cursor.execute('SELECT username FROM users WHERE username = ?', [un]).fetchall()
        if not un and user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is already taken'.format(un).encode()]

        else:
            page = '''<!DOCTYPE html>
            <form action = "/login" style = "background-color:gold"> 
            <h1> Login </h1>
            Username <input type = "text" name = "username"> 
            <br> 
            Password <input type = "password" name = "password"> 
            <br>
            <input type = "submit" value = "Log in">
            </form >
            <form action = "/register" style = "background-color:gold">
            <h1> Register </h1>
            Username <input type = "text" name = "secondusername"> 
            <br>
            Password <input type = "password" name = "secondpassword"> 
            <br>
            <input type = "submit" value = "Register">
            </form>'''

            if 'username' in params:
                cursor.execute('INSERT INTO users VALUES (?, ?)', [un, pw])
                connection.commit()
                headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
                start_response('200 OK', headers)
                if not un:
                    return [page.encode()]
                else:
                    return [page.encode(), 'Username {} was successfully registered <br> <a href="/account">Account</a>'.format(un).encode()]

            elif 'secondusername' in params:
                un2 = params['secondusername'][0] if 'secondusername' in params else None
                pw2 = params['secondpassword'][0] if 'secondpassword' in params else None
                # user = cursor.execute('SELECT username FROM users WHERE username = ?', [un2])
                headers.append(('Set-Cookie', 'session={}:{}'.format(un2, pw2)))
                start_response('200 OK', headers)
                if not un2:
                    return page.encode()
                else:
                    return [page.encode(), 'Username {} was successfully logged in <br> <a href="/account">Account</a>'.format(un2).encode()]
        # INSERT CODE HERE. Create two forms. One is to log in with a username and password, the other to register a new username and password.###

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
