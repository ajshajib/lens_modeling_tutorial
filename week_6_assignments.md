Get the lens imaging data in ‘.h5’ format for your team number and order number 
from the folder "mock_lens_images_2". Also, get the ‘psf.h5’ file from this same folder. 
   You have to model the lens system with `lenstronomy` in a Jupyter notebook 
(following the structure of "*Intro to lens modeling with lenstornomy.ipynb*") and 
submit the notebook to me to show your model. The notebook must show the model decomposition plots as in the Intro to lens modeling with lenstornomy.ipynb notebook. Your notebook may only run PSO and running MCMC is not required.

Now, here are some directions for you to do the lens modeling.

1. State your name and the people you got help from for this assignment at the top of 
the notebook in a Markdown cell.
2. Check the notebook "*Loading data from h5 files.ipynb*" to see how to read the *.h5 
   files.
3. Make sure the appropriate PSF is being provided to `lenstronomy` through `kwargs_psf`.
4. You need to add external shear to the `lens_model_list` with the profile name 
   ‘SHEAR’. The free parameters in this profile are: ‘gamma1’ and ‘gamma2’, and the fixed parameters are ‘ra_0’: 0, ‘dec_0’: 0. The upper and lower values for ‘gamma1’ and ‘gamma2’ are 0.3 and -0.3. (`lenstronomy` documentation: https://lenstronomy.readthedocs.io/en/latest/lenstronomy.LensModel.Profiles.html#lenstronomy.LensModel.Profiles.shear.Shear) 
5. You need to add the ‘SHAPELETS’ light profile to the `source_model_list`. The free 
   parameters are ‘beta’, ‘center_x’, and ‘center_y’. But, ‘center_x’ and ‘center_y’ needs to be joined with the ‘center_x’ and ‘center_y’ of the Sersic light profile in the `source_model_list`. The fixed parameter is ‘n_max’, you can try values between 4 and 6 for the fixed value of ‘n_max’. (`lenstronomy` documentation: https://lenstronomy.readthedocs.io/en/latest/lenstronomy.LightModel.Profiles.html#module-lenstronomy.LightModel.Profiles.shapelets)

If useful, you may try to get help from this tutorial notebook on lens modeling with 
`lenstronomy`: https://github.com/lenstronomy/lenstronomy-tutorials/blob/main/Notebooks/LensModeling/modeling_a_simple_Einstein_ring.ipynb. 