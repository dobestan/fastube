$(document).ready(function() {
  var commentsSectionElement = $("#comments-section");

  var commentsCountElement = $(commentsSectionElement).find("#comments-count");

  var commentsListElement = $(commentsSectionElement).find("ul");

  var commentsCreateFormElement = $(commentsSectionElement).find("form");
  var commentsCreateFormInputContentElement = $(commentsCreateFormElement).find("input[name='content']");

  var postSlug = $(commentsSectionElement).data("post-slug");
  var commentsAPIUrl = "/api/posts/" + postSlug + "/comments/";

  $.ajax({
    url: commentsAPIUrl,
    type: "GET",
    success: function(data) {
      var commentsCount = data.length;
      $(commentsCountElement).html(commentsCount);

      data.forEach(function(comment) {
        var commentUsername= comment.username;
        var commentContent = comment.content;

        var commentData = commentUsername + ": " + commentContent;

        var commentListElement = $("<li>").text(commentData);
        $(commentsListElement).append(commentListElement);
      });
    },
    error: function(data) {
    }
  });

  commentsCreateFormElement.submit(function() {
    var content = $(commentsCreateFormInputContentElement).val();
    alert(content);
    $(commentsCreateFormInputContentElement).val("");

    return false;
  });
});
