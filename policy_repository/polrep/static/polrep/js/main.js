function add_to_query(element, span) {
  var options = element.options;

  var value = element.options[element.selectedIndex].text;
  var query = $('#' + span);
  var existing_query = query.text();

  var exist_count = 0;

  for (var i = 0; i < options.length; i++){
    if (existing_query.includes(options[i].text) == true){
      exist_count += 1;
    }
  }

  if (exist_count == 0){
    query.append(value);
  }else {
    query.text(value);
  }
}

function check_eq_or_submit() {
  var full_query_length = 0;
  var qform = $('#policy-search-form');
  var form_action = $('#form-action-url').val();

  var query_tag_html = $('#full-query').html();

  var qspans = $('#full-query span').each(function(){
    full_query_length += $(this).text().length;
  });

  if (full_query_length == 0) {
    $('#empty-query-alert').show();
  }else {
    $('#empty-query-alert').hide();

    $('#query-tag-html').val(query_tag_html);

    console.log($('#query-tag-html').val());

    qform.attr("action", form_action);
    qform.attr("method", "post");
    qform.submit();
  }
}

function check_password_security() {
  // CHECK MIN 6 CHARS

  if ($('#password').val().length >= 6) {
    $('#min-chars').css('color', 'green');

    if ($('#min-chars').html().includes('<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>') == false){
      $('#min-chars').append(' <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>');
    }


  }

  // CHECK LOWERCASE

  if (/[a-z]/.test($('#password').val()) == true) {
    $('#min-lc').css('color', 'green');

    if ($('#min-lc').html().includes('<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>') == false){
      $('#min-lc').append(' <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>');
    }

  }

  // CHECK UPPERCASE

  if (/[A-Z]/.test($('#password').val()) == true) {
    $('#min-uc').css('color', 'green');

    if ($('#min-uc').html().includes('<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>') == false){
      $('#min-uc').append(' <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>');
    }

  }

  // CHECK NUMBERS

  if (/[0-9]/.test($('#password').val()) == true) {
    $('#min-num').css('color', 'green');

    if ($('#min-num').html().includes('<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>') == false){
      $('#min-num').append(' <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>');
    }

  }
}

function validate_registration() {
  var form = $('#registration-form');
  var action = $('#registration-form-action-url').val();

  if (($('#email').val() == $('#email-repeat').val()) &&
      ($('#password').val() == $('#password-repeat').val()) &&
      ($('#password').val().length >= 6) &&
      (/[a-z]/.test($('#password').val()) == true) &&
      (/[A-Z]/.test($('#password').val()) == true) &&
      (/[0-9]/.test($('#password').val()) == true)) {

    form.attr('action', action);
    form.attr('method', 'post');
    form.submit();
  } else {
    $('#form-errors-alert').fadeIn();
  }
}


$(document).ready(function(){

  $('#request-special-permissions-btn').click(function(){
    $('#request-special-permissions-btn').slideUp();
    $('#special-permissions-panel').slideDown();
  });

  $('#cancel-permissions-btn').click(function(){
    $('#request-special-permissions-btn').slideDown();
    $('#special-permissions-panel').slideUp();
  })

  // ===== Scroll to Top ====
  $(document).scroll(function() {
      if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
          $('#return-to-top').fadeIn(200);    // Fade in the arrow
      } else {
          $('#return-to-top').fadeOut(200);   // Else fade out the arrow
      }
  });
  $('#return-to-top').click(function() {      // When arrow is clicked
      $('body,html').animate({
          scrollTop : 0                       // Scroll to top of body
      }, 500);
  });
});
