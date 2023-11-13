def generate_html(project_title, num_inputs, dropdown_options, output_header):
    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_title}</title>
        <style>
            {style}
        </style>
    </head>
    <body>
        <div class="container">
            <form action="{{ url_for('predict')}}" method="post">
                <h1>{project_title}</h1>
                {input_fields}
                <button type="submit">Calculate {output_header}</button>
            </form>
            <br><br>
            <h3>{{ prediction_text }}</h3>
        </div>
    </body>
    </html>
    """

    # Generate input fields and dropdowns based on the number of inputs
    input_fields = ""
    for i in range(1, num_inputs + 1):
        input_fields += f'<h3>{dropdown_options[i-1]["label"]}</h3>'
        if dropdown_options[i-1]["type"] == "input":
            input_fields += f'<input id="input{i}" name="{dropdown_options[i-1]["name"]}" type="text" required="required">'
        elif dropdown_options[i-1]["type"] == "select":
            input_fields += f'<select name="{dropdown_options[i-1]["name"]}" required="required">'
            for option in dropdown_options[i-1]["options"]:
                input_fields += f'<option value="{option}">{option}</option>'
            input_fields += '</select>'

    # Styling
    style = """
        body {
            background-color: mediumseagreen;
            text-align: center;
            padding: 20px;
        }
        .container {
            border-radius: 14px;
            border-color: #2d4d4d;
            border-style: solid;
            font-family: cursive;
            text-align: center;
            background-color: #a8833d;
            font-size: medium;
            width: 50%;
            margin: 0 auto;
            padding: 20px;
        }
        h3 {
            margin: 10px 0;
        }
        input, select, button {
            width: 100%;
            height: 35px;
            border-radius: 10px;
            font-size: 16px;
            margin-bottom: 10px;
        }
        button {
            background-color: #005f5f;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #003333;
        }
    """

    # Insert input fields and styling into the template
    html_content = html_template.format(
        project_title=project_title,
        input_fields=input_fields,
        output_header=output_header,
        style=style
    )

    # Save to an HTML file
    with open(f'{project_title}_form.html', 'w') as file:
        file.write(html_content)

# Example usage
dropdown_options = [
    {"type": "input", "label": "Year", "name": "Year"},
    {"type": "input", "label": "Showroom Price (In lakhs)", "name": "Present_Price"},
    {"type": "input", "label": "Kilometers Driven", "name": "Kms_Driven"},
    {"type": "input", "label": "Number of Owners", "name": "Owner"},
    {"type": "select", "label": "Fuel Type", "name": "Fuel_Type_Petrol", "options": ["Petrol", "Diesel", "CNG"]},
    {"type": "select", "label": "Seller Type", "name": "Seller_Type_Individual", "options": ["Dealer", "Individual"]},
    {"type": "select", "label": "Transmission Type", "name": "Transmission_Mannual", "options": ["Manual", "Automatic"]}
]

generate_html("Car Price Prediction", len(dropdown_options), dropdown_options, "Selling Price")

