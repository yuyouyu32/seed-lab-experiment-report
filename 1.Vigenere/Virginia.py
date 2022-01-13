import re
import click

def encrypt_word(plainword, key, count):
    len_key = len(key)
    for index, plainchar in enumerate(plainword):
        if ord(plainchar) > 96:
            yield chr((ord(plainchar) + ord(key[(count + index) % len_key]) - 194) % 26 + 97)
        else:
            yield chr((ord(plainchar) + ord(key[(count + index) % len_key].upper()) - 130) % 26 + 65)


def encrypt_func(plaintext, key):
    count = 0
    for plainword in plaintext.split(' '):
        yield ''.join(encrypt_word(plainword, key, count))
        count += len(plainword)


def transfer_key(key):
    for key_char in key:
        yield chr(220 - ord(key_char))
        
@click.command()
@click.option('--encrypt/--no-encrypt', '-e', default=False, help='Encryption')
@click.option('--decrypt/--no-decrypt', '-d', default=False, help='Decryption')
@click.option('--text', '-t', default=None, type=str, help='The text to encrypt or decrypt.')
@click.option('--key', '-k', default=None, type=str, help='The key to encrypt or decrypt.')
@click.option('--file', '-f', default=None, type=str, help='The file_name to encrypt or decrypt.')
def main(encrypt, decrypt, file, text, key):
    """Virginia Cipher to encrypt or decrypt files or strings."""
    if (not encrypt and not decrypt) or (encrypt and decrypt):
        click.echo('Please choose to encrypt or decrypt!')
        return 
    if not key or not re.match(r'^[a-zA-z]+$', key):
        click.echo('Please input a legal key!')
        return
    if file:
        with open(file, 'r') as f:
            input_file = f.read()
        if not re.match(r'^[a-zA-z][a-zA-z ]+$', input_file):
            click.echo(f'Illegal characters in file {file}')
            return
        if encrypt:
            with open('cipher.txt', 'w') as f:
                f.write(' '.join(encrypt_func(input_file, key)))
        elif decrypt:
            with open('plain.txt', 'w') as f:
                f.write(' '.join(encrypt_func(input_file, ''.join(transfer_key(key)))))
    if text:
        if not re.match(r'^[a-zA-z][a-zA-z ]+$', text):
            click.echo(f'Illegal characters in {text}')
            return
        if encrypt:
            click.echo(f"plaintext: {text}\nkey: {key} \nciphertext: {' '.join(encrypt_func(text, key))}")
        elif decrypt:
            click.echo(f"ciphertext: {text}\nkey: {key} \nplaintext: {' '.join(encrypt_func(text, ''.join(transfer_key(key))))}")
            
                    
if __name__ == '__main__':
    main()

