# Your Agri Companion
## Winning Solution of DataVerse'21 conducted byt IETE-VIT and IEEE-WIE ,VIT Vellore.

![Promo-Facebook-Facebook cover photo](https://user-images.githubusercontent.com/55055042/144709226-7bc3e9bc-be57-4ebf-a358-3f40caef655e.jpeg)



## Using a Machine Learning Model to identify the optimal crop to grow, based on empirical data

An unbiased analysis based on information regarding factors such as the chemical composition of the soil, can prove to be a very
valuable asset, allowing farmers to make the right decisions to maximize their economic gain, as well as providing governing bodies with
the foresight required to incentvize farmers to grow certain crops, which can minimize the chance of overload on the food distribution
systems in the event of a natural calamity(eg: Famine).


### Demonstration
Our project is currently hosted on Streamlit, for purposes of demonstration: 
[Go to Demo](https://share.streamlit.io/sooryak12/dataverse-21/main/streamfile.py)

![gitdataver](https://user-images.githubusercontent.com/55055042/144709407-7d0696e9-ab77-4e7e-86b2-3098497668e0.png)



### Implementation

For selecting the best crop using the data we had to train our model, the Random Forest Approach stood out due to its excellent
F1 score, accuracy and low latency for a more responsive experience.

From our own search for appropriate datasets to the resources provided by the organizers of the Hackathon, we arrived at [this](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset) dataset, as it had the relevant data points (i.e the chemical composition of the soil and weather conditons), and was a large enough data set for
us to train and test our model on (with minimal duplication).

After cleaning up the data and ensuring the data points were normally distributed to ensure optimal performance of the model, we were able to perform feature decompostion
to visualize the chosen data, and to make decisions, arriving at the following t-Distributed Stochastic Neighbour Embedding (t-SNE) plot:

![tsnePlot](https://user-images.githubusercontent.com/70756241/144707926-c96f8fb7-28ca-4860-834e-e6086c2c570f.png)

5 fold cross validation was applied to detect and prevent overfitting of the model, using Tree based algorithms to best fit our data set.

While for the purposes of the Hackathon, a model in jupyter notebooks would have sufficed, deploying the app was important, not only for demonstration purposes, but also for
the project to be of any pracatical use. For the purpose of interpreting the model, the Shap library was added and used, so that we could have transparency on how our model
was making its decisions, as it is important for our statistical analysis:

![shapPlot](https://user-images.githubusercontent.com/70756241/144708130-747cf887-1dca-40f8-937b-8c55b970aa2e.png)

We also wanted to provide a way for anyone to compare their own choice in crops to that predicted by the model, so they could compare and contrast the improvements they can
attain in terms of crop yield by selecting a more appropriate crop, allowing farmers to make their own well-informed decisions. To provide the statitical analysis, we made of
pandas, streamlit's plotting functionality and the following datasets:
- [Crop production in India](https://www.kaggle.com/abhinand05/crop-production-in-india)
- [Agriculture crop production in India](https://www.kaggle.com/srinivas1/agricuture-crops-production-in-india)

### Scope For Future Growth

While the dataset that we chose to train our model was an excellent starting point, it is still limited in the number of crops and varieties that it represents. Therefore,
a larger dataset could be used in the future to further improve the accuracy of the predictions that our model makes.

We also recognize that it is impractical to ask a 'layman' to measure values such as the nitrogen content of the soil, pH value of the soil etc., for the purposes of manually 
entering these values into our web-app.

Both these issues can be greatly remedied by the design and implementation of an IOT component into this project, consisting of low cost parts and sensors(Arduinos and the 
required sensors) to create low power data collecting units, which can be deployed to a vast number of participants in the program. This would give us an ever growing number
of data points to analyze, which could be used to identify recent trends in the changing soil and weather conditions for our model.
This would also simplify the process of anyone using the portal, as one of these 'data units' could be linked to an account, which could automatically enter in the required
input values, eliminating the tedious manual step of having to enter the values ourselves.

An example of such a device could be:

![image](https://user-images.githubusercontent.com/70756241/144708562-aa3cbd8d-823a-478e-956e-009ceb4e0aa3.png)



### Technology Stack
Our solution was built using:
- [Python](https://www.python.org/)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/)
- [Shap](https://github.com/slundberg/shap)
- [Streamlit](https://streamlit.io/)


 
