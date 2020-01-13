# read name.txt and contain my name into "my_name"
with open('name.txt') as f:
    my_name = f.read()

# open hello.txt and write the greeting
with open('hello.txt', 'w') as g:
    g.write('Hello, my name is ' + my_name + '.')