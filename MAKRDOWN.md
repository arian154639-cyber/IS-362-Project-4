Note: This project was submitted late. According to the syllabus, late projects are allowed, but lose 5 points for each
hour late. This project was submitted to GitHub in its final form and submitted to Brightspace prior to 3AM.

Analysis: 
My conclusion, based on the test scores, is that odor is a far better predictor of edible status than bruising. 
This is because odor scored above 98% on the test set, while bruising only scored approaximately 74%. My further 
recommendation for analysis is to test the other predictor variables. I am curious about gills in particular, as 
I have seen that sometimes, gills can be used to tell apart different species, but that is unconfirmed. Additionally, 
different test models may be a better fit here. I chose KNN because it was what the tutorial video I watched covered, 
but perhaps one of the others such as logistic regression could be more accurate.

Process Notes:
I used the videos suggested in the project instructions to get a better understanding of the assignment. 
I then searched for more research materials from sources such as GeeksforGeeks and W3Schools. I chose to
use KNN because that seemed like a simple solution and it was what the tutorial videos covered. To start
off, the script uses part of my script from the previous assignment. I then loaded the cleaned dataset as 
KNN_dataframe so that I could make use of the data. I then defined X (the predictor, such as Odor) and 
y (the target, edible status). Then, following the GeeksforGeeks tutorial, I used train_test_split to 
separate some data into a training set and some into a testing set. I chose an 80/20 ratio because according 
to my research, 80/20 and 70/30 are common ratios here. Next, I created the KNN and then trained the model.
Finally, I tested the model. I did this twice because although this does violate DRY, I wanted to focus more
on understanding and less on efficiency this time.

I didn't follow the tutorials completely. For example, one of them made use of scaling, but my research led 
me to conclude I didn't need that here because the ranges for each predictor were small anyway. I did some testing 
such as using different values for the nearest neighbor, but that didn't seem to affect test scores. I initially 
thought perhaps random state would matter for scoring, but I learned that it did not (the source itself only 
mentioned reproducibility, but I wanted to see if it would affect test scores). I also tested various different 
train/test ratios, this was what affected scoring, but the differences seemed slight. Admittedly, this may be due 
to me only using those aforementioned common ratios of 80/20 and 70/30 instead of something like 10/90 or 20/80. 

