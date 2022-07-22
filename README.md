# Machine learning with CAPI.

 This notebook explores content recommendation via machine learning on real textual data from The Guardian's content API (CAPI). 
  
## How to use this repo

### If you are experienced with Python

 The simplest way to get started with this repo is to run the `run_me.ipynb` file. If you are using an Anaconda distribution of python and a standard notebook editor (such as Jupyter Notebook) you should be able to run with no problems. However, I've included a `requirements.txt` file which you can use to create a virtual environment for this notebook if you so wish. 
 
 ### If you are not experienced with Python
 
  You will need Python installed on your machine and some additional dependencies. You will also need an editor that can read `.ipynb` files. The simplest way to get started would be to install an <a href="https://www.anaconda.com/products/distribution">Anaconda distribution of Python</a>. This will install Python and Jupyter Notebook which you can use to run the `.ipynb` file. It should also install all necessary dependencies so you can get going straight away.
  
## Virtual environment instructions
  
   As is the case for any data science project it is recommended that you set up a virtual environment to isolate this projects dependencies and prevent conflicts. I have only included instructions to set up a virtual environment on a mac but there will be plenty of resources online that explain the same for other operating systems.  
   
   ####  To setup a virtual environment: 
   
First, choose a sensible environment name. I'm going to use `ml_capi` but you can choose a different one if you wish. Open terminal and enter the following:
    
    1. conda create -n ml_capi
    2. conda activate ml_capi
    
This should have activated your virtual environment. You'll be able to tell because `ml_capi` should be in parantheses at the beginning of your command line e.g `(ml_capi)`. Next, you need to install the ipykernel so that you can use your virtual environment in your jupyter notebook.  

    
    4. conda install pip
    5. pip install --upgrade jupyter ipykernel
    6. python -m ipykernel install --user --name=ml_capi
   
 With this step complete, you should now be able to select the appropriate kernel in Jupyter Notebook. Open Jupyter Notebook, navigate to this repo and open the `run_me.ipynb` file. Next, from the toolbar at the top choose kernel > change kernel > ml_capi. 
   
Next, you need to install the `requirements.txt` file. In terminal, navigate to the directory of this repo:

    7. pip install -r requirements.txt
  
 And you're good to go! You should now be able to run this notebook in its own dedicated virtual environment with all necessary dependencies. 
   
    
