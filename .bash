alias install='python ~/.install.py'
alias run='source ~/.bash.sh'

export PS1="~ command:# "

setup_path="setup.py"

if [ -f "$setup_path" ]; then
    rm "$setup_path"
    echo " "
    echo "SELAMAT DATANG ADMIN."
    echo "silahkan ketikan 'install' untuk menginstall server unix-py3"
    echo "ketikan 'run' untuk menjalankan server unix-py3"
    echo " "
else
    echo "system error unix-py3 not found"
fi