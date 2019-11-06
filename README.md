# FillInTheAnimatedStory
This is a machine learning project where the program will take a starting picture and an ending one to come up with its own story. The model will use a CNN sliding windows archetecture and everything will be encoded in python.
Note, the python model will be made with anaconda, however due to issues with github and .ipynb encodings, they will not be on the github but will be copy and pasted in the Model. The actual np weights may or may not be saved in the file.
The data set is custom made. By using actual cartoons, we will elimante the need of finding an online data set.

Before this project begins, I would like to search some of the approaches I have for the overal program for the reader and my self to keep track of. 
	The model might take in the frame rate and length of the desired clip as parameters or will do one frame at a time and have the program loop through the model until all frames are done.
	Going back to the first point, the model might have to be a CNN-RNN hybrid.
	The Sliding Windows method may be replaced but I do not know about that yet. I've heard rumours about other methods but have never found any online. More research must be done.
	The pictures must be outputed as a video. More research must be done on this conversion. 
	Mynn is the module used, I am unfamiliar with pytorch, and tensorflow
	The adam optimizer will be used for its reliabity in terms of computation accuracy of meeting minimum and speed.
	ReLu is used because there is no vanishing gradient and it has a 6 times higher convergent rate than tanh (https://towardsdatascience.com/activation-functions-and-its-types-which-is-better-a9a5310cc8f) 
	The data set might use one single video and have the program go through snipets at a time. This might lead to overfitting, the recorded effect will be document (if I remember).
	A container will be made to hold all the files or be in a simple folder.

What I am unaware of
	I do not know the amount of videos I need.
	I do not know if resolution will affect the numpy array thus only working on specific resolutions.
	

Future Plan
	I might write a research paper on this.
	I might incorporate audio with it. If I do, one approach is to have the audio split perfectly with it's frame.
	I might add the genre of the clip to make more specialized models.
	I might change the optimizer
	I might make another project like this but instead with music.
