#Welcome

This package is for a simple auto complete algorithm. Contained within is a python module that 
houses the main class, AutoComplete, which trains auto-complete databases. Likewise, this 
package installs two binaries that use this python3.7.7 module backend: 

    auto-train
    auto-complete
    
#Installation

Installing this package is very simple. The script_args has all ready been set for you in the 
install.py file. Simply run that file to install the module and binaries. 

    > python install.py
    
or

    > chmod u+x install.py
    > ./install.py
    
If you want to run the install.py file as a setup.py instead, simply remove the script_args
in the install.py file (or comment it out). Then you will get typical setup.py behavior. 

Autocomplete was built on entirely standard packages, except sortedcontainers. Please pip
install sortedcontainers before using this pacakge. The installer should warn you of this
as well, if you are missing this package. 

    > pip install sortedcontainers

#Bin Directory

It is assumed that the user has setup their python installation to work with custom scripts. 
For example, if you have anaconda installed, you should probably have ~/anaconda3/bin added
to your PATH (if you didn't let anaconda do that during installation). Another example is 
if you perform a local setup.py (--local), then you should probably have ~/.local/bin added 
your PATH. If you have installed other python packages before and their binaries work for 
you, then this should work just fine. But if you can't find the binaries after install, then 
double check that your PATH includes the location where your python installation installs custom 
python binaries. 

#Removing

If you wish to remove the package, as usual, simply pip uninstall the package. 

    > pip uninstall AutoComplete

#Usage

This package can be used in one of two ways. Either interactively (as in importing and using 
the backend) or from the command line. 

###Interactively

The main class is located at autocomplete.autocomplete.AutoComplete and is used to train
autocomplete databases and then ask about the autocompletion of various partial strings. 
You can of course, use the backend to write your own custom scripts, jupyter notebooks, 
or use interactively. 

Example: 

    > ipython3
    >> from autocomplete.autocomplete import AutoComplete
    >> AutoComplete?
    >> x = AutoComplete()
    >> x.train('thing stuff this that the other thing and cool stuff')
    >> x.autocomplete('t')
    >> x.autocomplete('t',True)
    >> x.autocomplete_dict('t')
    >> x.autocomplete_dict('T')
    >> y = AutoComplete('other cool things to train on that complete things')
    >> y
    >> z = x + y
    >> z
    >> z.autocomplete_dict('Thin')
    >> z.autocomplete_dict('thin')
    >> z.train('add more words to Train on and Things with Thing.')
    >> z.autocomplete_dict('thin')
    >> z.autocomplete_dict('TR')
    
###Command Line

Two scripts have been built off this backend and can be found at autocomplete.autocomplete.bin
for reference. After install, they should be available from the command line from any working
directory. These scripts default to creating and appending to a database within the current
working directory; this of course can be changed with the -d option. 

    > auto-<TAB COMPLETE>
    > auto-train --help
    > auto-complete --help
    > auto-train -t "The third thing that I need to tell you is that this thing does not think thoroughly."
    > auto-complete -t thi
    > auto-complete -t thi -l 2
    > auto-complete -t thi -l 2 -c
    > auto-complete -t thi -c 
    > auto-complete -t nee -c 
    > auto-complete -t th -c 
    > auto-train -t "add more words to the database"
    > auto-complete -t ad -c
    > auto-train -t "start a new database with a custom name" -d test
    > auto-complete -t cu -c -d test
    > auto-train -t "(add) more! stuff. to database TEST" -d test
    > auto-complete -t te -c 
    

