# CNDS-DATA
CNDS is a system detecting promotional infection based on Convolutional Neural Network and Natural Language Processing.

Here you can see the data we used in this system, including the training data and validating data for the process of training the model, the testing data for checking the performance of the model.

Training data and Validation data is both from the Baidu company. Testing data is from Ali.

Training data : validation data = 5 : 1

# Detecting Service by Web service
You can open the link of "202.112.51.38", then you can type in a url link in the input box on the webpage.

For example, typing in a url which is black: http://www.66kj.com/.

![](https://github.com/NISL-DETECT/CNDS-DATA/blob/master/ex_black.png)

Then you will receive the result like what we show in the following picture:

![](https://github.com/NISL-DETECT/CNDS-DATA/blob/master/ex_black_re.png)

And we will record the screenshor and the html file, you can click the link to view the screenshot and html file.

![](https://github.com/NISL-DETECT/CNDS-DATA/blob/master/screenshot.png)

![](https://github.com/NISL-DETECT/CNDS-DATA/blob/master/html_black.png)

# Detecting Service by TCP Request
This service will be shut down, you can test the system by the Web service we mentioned before.

You should use 'client.py' to send a TCP request with a url to be detected to our TCP server and then you will receive the result of the category of this url.

The IP address for this service is 202.112.51.36.
The port opened for this service in our TCP server is 9998.

The code "client.py" should run under python2.x environment.

The step you detect a url with our trained model is:

First, you should run the code "client.py" with the url to be detected. For example:

```python 
python client.py http://www.66kj.com/
``` 

Then, you will receive the result.
The delay between sending request and receiving response is 2~3 seconds.

This is an example:

![](https://github.com/NISL-DETECT/CNDS-DATA/blob/master/test.png)

The example URL in this example is a Chinese gambling website shown in the following picture:

![](https://github.com/NISL-DETECT/CNDS-DATA/blob/master/gambling_example.png)
