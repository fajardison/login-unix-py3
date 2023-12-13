alias install='python ~/.install.py'
alias run='source ~/.bash.sh'

export PS1="~ command:# "

setup_path="setup.py"

if [ -f "$setup_path" ]; then
    rm "$setup_path"
    echo " "
    echo "SELAMAT DATANG ADMIN."
    echo "jalankan perintah 'install' untuk menginstall source code"
    echo "setelah menginstal source code jalankan perintah 'run' untuk menjalankan unix-py3"
    echo " "
else
    echo "system error login-unix-py3 not found"
fi
