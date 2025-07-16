from pyscript import display, document  # importing the display module


print('Hello Earth')  # will be displayed in the console
display('Hello World!')  # will be shown in the webpage

def greeting_user(a):  # creating the function name
    document.getElementById('output').innerHTML = ''
    username = document.getElementById('data1').value

    display(f'Welcome {username} !', target='output')
