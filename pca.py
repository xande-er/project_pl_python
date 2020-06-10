
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import scipy.io as sio
import matplotlib.image as image
import pandas as pd
import matplotlib.pyplot as plt

X = sio.loadmat('ex7faces.mat')
X = pd.DataFrame(X['X'])
X_norm = normalize(X)

pca = PCA(.99)
lower_dimension_data = pca.fit_transform(X_norm)
lower_dimension_data.shape

approximation = pca.inverse_transform(lower_dimension_data)
approximation.shape
approximation = approximation.reshape(-1,32,32)
X_norm = X_norm.reshape(-1,32,32)

for i in range(0,X_norm.shape[0]):
    X_norm[i,] = X_norm[i,].T
    approximation[i,] = approximation[i,].T

fig4, axarr = plt.subplots(3,2,figsize=(8,8))
axarr[0,0].imshow(X_norm[0,],cmap='gray')
axarr[0,0].set_title('Original Image')
axarr[0,0].axis('off')
axarr[0,1].imshow(approximation[0,],cmap='gray')
axarr[0,1].set_title('99% Variation')
axarr[0,1].axis('off')
axarr[1,0].imshow(X_norm[1,],cmap='gray')
axarr[1,0].set_title('Original Image')
axarr[1,0].axis('off')
axarr[1,1].imshow(approximation[1,],cmap='gray')
axarr[1,1].set_title('99% Variation')
axarr[1,1].axis('off')
axarr[2,0].imshow(X_norm[2,],cmap='gray')
axarr[2,0].set_title('Original Image')
axarr[2,0].axis('off')
axarr[2,1].imshow(approximation[2,],cmap='gray')
axarr[2,1].set_title('99% variation')
axarr[2,1].axis('off')
plt.show()