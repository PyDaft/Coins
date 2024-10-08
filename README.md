<H1> Capstone Project: Coins Image Processing & Summation Problem </H1>
<br>
<H2> About the Project </H2>

The image of coins.jpg is a collection of Britsih Pennies of different denomination. The idea is to identify different circular (omit the one with polygon shape) and add up the denominations and print the final value of all the coins on the processed image.
<br>
<h4>
  1. Numpy - for image processing and identifying coins basis their brightness <br>
  2. OpenCV - for finding the coordinates of different circles and printing the respective values of the coins on the image itself
</h4>
<br>
<h2> How I approached the problem</h2>

<br>
1. This code uses OpenCV to process the image.
2. The image is converted to grayscale and a Gaussian blur is added for easier processing.
3. The circles in the image were identified using the Hough circles method (specification was pulled from the OpenCV documentation).
4. An outer perimeter was drawn along the rim and a circle was drawn in the center of each coin.
5. The coin count number was also added to each coin.
6. The radius and brightness of each coin is then retrieved.
7. The coins' brightness and radius is compared, and the coins are categorized accordingly.
8. The total value of the coins is displayed in the upper left-hand corner of the image.
