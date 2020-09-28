import webbrowser
import os
print ()
f = open('creditcardinfo.html','w')
 
message = """<html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Credit Card Info</title>

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

  <script type="text/javascript" src="https://js.verygoodvault.com/vgs-collect/1/ACtCRq2g2aZtdR8tqiijnLgo.js"></script>

  <style>
    body {
      padding: 25px;
    }

    span[id*="cc-"] {
      display: block;
      height: 40px;
      margin-bottom: 15px;
    }

    span[id*="cc-"] iframe {
      height: 100%;
      width: 100%;
    }

    pre {
      font-size: 12px;
    }

    .form-field {
      display: block;
      width: 100%;
      height: calc(2.25rem + 2px);
      padding: .375rem .75rem;
      font-size: 1rem;
      line-height: 1.5;
      color: #495057;
      background-color: #F5F5F5;
      background-clip: padding-box;
      border: 1px solid #ced4da;
      border-radius: .25rem;
      transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
    }

    .form-field iframe {
      border: 0 none transparent;
      height: 100%;
      vertical-align: middle;
      width: 100%;
    }

    p {
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
<main>
  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-4">
      <div class="row card card-outline-secondary">
        <div class="card-body">
          <h3 class="text-center">Credit Card Payment</h3>
          <hr>
          <div class="alert alert-info p-2">
            Please fill in and submit a form to see redacted data in response window.
          </div>
          <form id="cc-form">
            <div class="form-group">
              <label for="cc-name">Name on the card</label>
              <span id="cc-name" class="form-field">
                <!--VGS Collect iframe for card name field will be here!-->
              </span>
            </div>
            <div class="form-group">
              <label for="cc-number">Card number</label>
              <span id="cc-number" class="form-field">
                <!--VGS Collect iframe for card number field will be here!-->
              </span>
            </div>
            <div class="form-group">
              <label for="cc-cvc">CVC</label>
              <span id="cc-cvc" class="form-field">
              <!--VGS Collect iframe for CVC field will be here!-->
              </span>
              <p>* 3 or 4 digits usually found on the signature strip or back of the card</p>
            </div>
            <div class="form-group">
              <label for="cc-expiration-date">Expiration date</label>
              <span id="cc-expiration-date" class="form-field">
              <!--VGS Collect iframe for expiration date field will be here!-->
              </span>
            </div>

            <!--Submit credit card form button-->
            <button type="submit" class="btn btn-success btn-block">Submit To Continue</button>
          </form>
        </div>
      </div>
    </div>
    
    
    
  </div>
</main>

<!--Include script with VGS Collect form initialization-->
<script>
  // VGS Collect form initialization
  const form = VGSCollect.create("tntvdd0jmyk", function(state) {});

  // Create VGS Collect field for credit card name
  form.field('#cc-name', {
    type: 'text',
    name: 'card_name',
    placeholder: 'Joe Business',
    validations: ['required'],
  });

  // Create VGS Collect field for credit card number
  form.field('#cc-number', {
    type: 'card-number',
    name: 'card_number',
    successColor: '#4F8A10',
    errorColor: '#D8000C',
    placeholder: '5111 6111 7111 8111',
    validations: ['required', 'validCardNumber'],
  });

  // Create VGS Collect field for CVC
  form.field('#cc-cvc', {
    type: 'card-security-code',
    name: 'card_cvc',
    placeholder: '344',
    validations: ['required', 'validCardSecurityCode'],
  });

  // Create VGS Collect field for credit card expiration date
  form.field('#cc-expiration-date', {
    type: 'card-expiration-date',
    name: 'card_expirationDate',
    placeholder: '01 / 2022',
    validations: ['required', 'validCardExpirationDate']
  });

  // Submits all of the form fields by executing a POST request.
  document.getElementById('cc-form')
    .addEventListener('submit', function(e) {
      e.preventDefault();
      form.submit('/post', {
      }, function(status, data) {
        document.getElementById('result').innerHTML = JSON.stringify(data.json, null, 4);
      });
    }, function (errors) {
      document.getElementById('result').innerHTML = errors;
    });
</script>
</body>
</html>"""
 
f.write(message)
f.close()

#Change path to reflect file location
filename = 'file:///'+os.getcwd()+'/' + 'creditcardinfo.html'
webbrowser.open_new_tab(filename)