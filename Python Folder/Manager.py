def CleanData(x):
    '''
    Cleans the picture data so that it is compatable with the model
    It forces the picture to have 3 dimensions, the last two are padded or cut to [X,1024,1024]
    It turns a gray scale into a colored image

    Parameter
    ---------
    X is a numpy array [3,L,W] or [1,L,W]

    Output
    ---------
    Y a numpy array [3, 1024, 1024]
    3 represents the RGB value
    1024 represents the length of the picture
    768 represents the width of the picture
    '''
    assert isinstance(x, np.ndarray), "You need your picture data to be a numpy array"
    assert len(x.shape) == 3, "Your picture data is messed up for some reason there is another dimension"
    if x.shape == (3, 1024, 1024):
        # Your data fits the requirements
        return x
    if x.shape[0] < 3:  # Meaning this is a noncolored image
        print (x.shape[0])  # Dummy function
    # if x.shape[1]<1024 or x.shape[2]<1024:
    #    dummy = np.zeros((3,1024,1024))
    #    dummy[:,:x.shape[1],:x.shape[2]] = x
    #    x = dummy

    if x.shape[1] < 1024:
        dummy = np.zeros((3, 1024, x.shape[2]))
        dummy[:, :x.shape[1], :x.shape[2]] = x
        x = dummy
    if x.shape[2] < 1024:
        dummy = np.zeros((3, x.shape[1], 1024))
        dummy[:, :x.shape[1], :x.shape[2]] = x
        x = dummy

    if x.shape[1] > 1024 or x.shape[2] > 1024:  # Cut off function
        x = x[:, :1024, :1024]

    # if x.shape[1]<1024: #length
    #   x1 = 1024 - x.shape[1]
    #  add= np.zeros((3,x1,x.shape[2]))
    # x= np.vstack((x,add))
    # if x.shape[2]<1024: #width
    #   x2 = 1024- x.shape[2]
    #  add = np.zeros((3,x.shape[1],x2))
    # x= np.hstack((x,add))

    assert x.shape == (3, 1024, 1024), "For some reason your data cant be cleaned"
    return x

def convertImtoNdArray (image):
    return image.flatten().astype(np.float32)-np.mean(image)/np.std(image)
#we want to flatten the array so that we can have one input layer. Subtracting by the mean then dividing by the std makes it normalized. The float is for precision by we dont want to much precision, so 32 is used.
# Sould be uppercase pi (index)
#S