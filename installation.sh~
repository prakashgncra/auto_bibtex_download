# define various paths
bashfun='.github_extras/bash_functions.sh'
basedir='.github_extras/auto_bibtex_download/'

# Make directory move files is necessary
mkdir -p ~/$basedir
cp Auto_bibtex_copy.py ~/$basedir'Auto_bibtex_copy.py'
touch ~/$bashfun
chmod +x ~/$bashfun

# Write the bash function, aliases for system wide access
echo "" >> ~/$bashfun
echo "#--------------- Automatic Bibtex Download function ----------------" >> ~/$bashfun
echo "" >> ~/$bashfun
echo 'function auto_bibtex_download()' >> ~/$bashfun
echo '{' >> ~/$bashfun
echo 'python '~/$basedir'Auto_bibtex_copy.py ${1} ${2} ${3}' >> ~/$bashfun
echo '}' >> ~/$bashfun
echo '' >> ~/$bashfun
echo "" >> ~/$bashfun


# Check if .github_extras/bash_functions.sh is source in bashrc
SOURCE_STRING='source ~/'$bashfun
if [[ ! -z $(grep "$SOURCE_STRING" ~/.bashrc) ]]
then 
source ~/$bashfun
echo "File "$SOURCE_STRING" is sourced ..."
else
echo $SOURCE_STRING >> ~/.bashrc
source ~/.bashrc 
echo "File .bashrc and "$SOURCE_STRING" is sourced ..."
fi
