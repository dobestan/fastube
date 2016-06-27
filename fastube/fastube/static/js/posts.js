$(document).ready(function() {
  var commentsSectionElement = $("#comments-section");
  var commentsCreateFormElement = $(commentsSectionElement).find("form");
  var commentsCreateFormInputContentElement = $(commentsCreateFormElement).find("input[name='content']");

  commentsCreateFormElement.submit(function() {
    var content = $(commentsCreateFormInputContentElement).val();
    alert(content);
    $(commentsCreateFormInputContentElement).val("");

    return false;
  });
});
