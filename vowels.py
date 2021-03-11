
import click

@click.command()
@click.option("--filename",prompt="type file name")
def fetchVowels(filename):
    with open(filename) as f:
        contents = f.read()
    string = contents.casefold()
    stringOfVowels="aeiou"
    vowels = {}.fromkeys(stringOfVowels, 0)
    Totalcount=0
    for ch in string:
        if ch in vowels:
            vowels[ch] += 1
            Totalcount=Totalcount+1

    click.echo(f"{vowels} Total count={Totalcount}")

if __name__=='__main__':
    fetchVowels()


