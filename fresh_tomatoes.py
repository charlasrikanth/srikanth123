#!/usr/bin/env python
import webbrowser
import os
import re
print("content-type:text/html \n")
# Styles and screpting for the page
main_page_head = '''
<!DOCTYPE html>
<html>
<head >
     <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <style>
    .modal {
    display: none;
    position: fixed;
    z-index: 1;
    padding-top:100px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.4);
            }
.modal-content {
    margin: 5% auto;
    padding: 20px;
    width: 560px;
    min-height:500px;
}


.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    background-color: black;
    text-decoration: none;
    cursor: pointer;
    padding-left:5px;
    padding-right:5px;
}

      .container{
        display: flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
       }
     .box{
          width:100%;
          min-height:150px;
          cursor:pointer;
        }
      @media screen and (min-width :450px)  {
      div.v1:hover{
             border:1px;
             background-color:red;
             border-radius:20%;
             }
       div.v2:hover{
             border:1px;
             background-color:blue;
             border-radius:20%;
             }
       div.v3:hover{
             border:1px;
             background-color:green;
             border-radius:20%;
             }
       div.v4:hover{
             border:1px;
             background-color:yellow;
             border-radius:20%;
             }
    div.v5:hover{
             border:1px;
             background-color:pink;
             border-radius:20%;
             }
       .v1{width:50%;}
       .v2{width:50%;}
       .v3{width:50%;}
       .v4{width:50%;}
       .v5{width:50%;}
       h1 {background-color:black;}
        }
      h1 {background-color:black;
         font-family:arial,cursive;}
      </style>
         <div id="myModal" class="modal">
 <div class="modal-content">
                <span class="close">&times;</span>
                 <iframe id="f" width="560" height="315"
                 src="" frameborder="0" allow="autoplay;
                 encrypted-media" allowfullscreen></iframe>
          </div>
</div>
   <script>
   // Get the modal
var modal = document.getElementById('myModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
    onc = function(c) {
    modal.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("f").setAttribute("src",c);
}

// When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    }
}
</script>
</head>
'''
# The main page layout and title bar
main_page_content = '''
<body style = "text-align:center">
   <div class = "center"><h2>Trailers</h2>
</div>
<div class="container">
   <div class="box v1"
   onclick="onc('EQdOOTQnuvk')">
   <img vspace="30" src="https://bit.ly/2GD3KRc"
   alt="fig1" style="width:60%"height="300" hspace="30";>
   <h2 style="color:white;">spider man-1</h2></div>
   <div class="box v2"
   onclick="onc('BWsLc3j1AWg')">
   <img vspace="30" src="https://bit.ly/2KCR8Mk"
   alt="fig2" style="width:60%"height="300" hspace="30";
   ><h2 style="color:white;">spider man-2</h2></div>
   <div class="box v3"
   onclick="onc('-tnxzJ0SSOw')"> <img vspace="30";
   src="https://bit.ly/2wXjr6l"
   alt="fig3" style="width:60%" height="300" hspace="30">
   <h2 style="color:white;">Amazing spider man</h2>  </div>
   <div class="box v4"
   onclick="onc('n9DwoQ7HWvI')"> <img vspace="30"
   src="https://bit.ly/2Ivqngi"
   alt="fig4" style="width:60%"height="300"  hspace="30">
   <h2 style="color:white;">Spider man home coming</h2></div>
   <div class="box v5"
   onclick="onc('8QYZQiBVx18')">
   <img vspace="30" src="https://bit.ly/2s0z5YO"
   alt="fig5" style="width:60%"height="300"  hspace="30">
   <h2 style="color:white;">Spider man home coming-2</h2></div>
        </div>
</body>
</html>
'''
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center"
data-trailer-youtube-id="{trailer_youtube_id}" data-target="#trailer">
<img src="{poster_image_url}" width="220" height="342">
<h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_title_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0)
                              if youtube_id_match else None)
        # Append the title for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id)
        return content


def open_movies_page(movies):
    # create or overwrite the output file
    output_file = open('fresh tomatoes.html', 'w')

    # Replace the movie titles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_title_content(movies))

    # Output the file
    output_file.write(main_page_head+rendered_content)
    output_file.close()

    # Open the output file in the browser(in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)

