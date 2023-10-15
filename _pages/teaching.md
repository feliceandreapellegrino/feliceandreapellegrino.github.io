---
layout: page
permalink: /teaching/
title: teaching
description: general information about the courses I teach. 
nav: true
nav_order: 5
---

## computer vision and pattern recognition 2023
The course will start on **Tuesday, October 3, 2023**.

The timetable is as follows:

| day         | time        | room     |
| :---        |    :---   |          :--- |
| Tuesday      | 12-14       | TB, building C5   |
| Thursday   | 12-14        | TB, building C5      |
| Friday   | 11-12        | TB, building C5      |

&nbsp;  

Students are encouraged to [register for the course on Moodle](https://moodle2.units.it/course/view.php?id=11338">https://moodle2.units.it/course/view.php?id=11338). There, I will publish the updated teaching material and the tutorial code. Furthermore, all communications relating to the course will be sent to Moodle subscribers.

## office hours
Send me an email to arrange a meeting (possibly specifying your preferred day and time).

How to get to my room:
<video src="https://user-images.githubusercontent.com/47215410/271945836-be66b942-61df-4217-854e-b4dcfad3a40b.mp4" data-canonical-src="https://user-images.githubusercontent.com/47215410/271945836-be66b942-61df-4217-854e-b4dcfad3a40b.mp4" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px">
</video>


 <td>
    <img name="canvas" />
</td>

<script>
//create an array named imagesArray that contains the seven image file names
//dog.jpg, fox.jpg, mouse.jpg, alligator.jpg, fish.jpg, parrot.jpg and cat.jpg
var imagesArray = ["/assets/img/prof_pic.jpg", "/assets/img/code-screenshot.png"];
//create a function named displayImage
//it should not have any values passed into it
function displayImage(){
    //the first statement should generate a random number in the range 0 to 6 (the subscript values of the image file names in the imagesArray)
    var num = Math.floor(Math.random() * 3); // 0...6
    //the second statement display the random image from the imagesArray array in the canvas image using the random number as the subscript value
    document.canvas.src = imagesArray[num];
}
//remember the subscript values of the array are 0 to 6 (seven elements) zero based array
//you will have to subtract 1 from the random number generated to account for the zero based array
</script>