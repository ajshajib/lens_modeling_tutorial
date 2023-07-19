1. Finish working on the notebook “*Linear regression with MCMC.ipynb*”.
2. Look at the python script “*city_temperatures.py*”. Identify the PEP8 violations in 
   this script.
3. If you have counted a total of 10,000 photoelectrons over 10 minutes created from 
   incoming photons at a CCD pixel of a telescope’s camera, what is the noise level or uncertainty in that photoelectron count?
4. Retrieve your specific data file for your team number and order number from 
   the folder "*data/elliptical_galaxy_images*". You 
   can read the data file using `numpy.loadtxt()` function. The file contains a 2D image of an elliptical galaxy. In other words, each pixel contains a flux value. The point spread function (PSF) is a Gaussian with 0.3 arcsecond FWHM. Plot `numpy.log10(image)` using the `matplotlib.pyplot.matshow()` function. Each pixel size is 0.05 arcsecond. How large is the full image in the arcsecond unit?
5. The unit of each pixel’s flux value is electron/second. The total exposure time for 
   this image is 600 seconds. What is the noise level in each pixel in the electron/second unit? Plot the signal-to-noise ratio map for the image using `matshow()`.
6. Model the flux distribution in the image using an elliptical Sersic function. Don’t 
   forget the PSF in your model. You will need to find the uncertainties of the 
   model parameters using MCMC. Fix $n_{\rm Sersic}$ = 4 in your model, but find the 
   best-fit values for other parameters. The other model parameters and their priors are: 
   1. x-centroid, $x_0$: prior up to you to choose
   2. y-centroid, $y_0$: prior up to you to choose
   3. scale radius, $R_{\rm Sersic}$: uniform between 0 arcsec and 3 arcsec
   4. axis ratio, $q$: uniform between 0.4 and 1
   5. position angle, $\phi$:  uniform between 0 and $\pi$
   6. amplitude: prior is up to you to choose
7. Make a residual plot, where residual =  (image - model) / noise level. Choose the 
      colormap “RdBu_r” and set `vmax = 3, vmin = -3` in the `matshow()` function. 
   What’s the chi-squared ($\chi^2$) value for your fit? What’s the reduced 
   chi-squared?
8. What is the half-light radius or the effective radius of this galaxy?
