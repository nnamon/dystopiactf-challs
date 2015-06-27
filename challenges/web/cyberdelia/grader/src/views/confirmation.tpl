<html>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
    <style>
        body {
            background-color: #222222;
        }

        h1, h2, h3 {
            color: #ffffff;
        }

        p {
            color: #cccccc;
        }
    </style>
    <body>
        <div class="pure-g" style="margin-left: 30px;">
            <div class="pure-u-1 pure-u-md-1-3">
                <img src="images/cyberdelia.png" style="width:50%; margin-top:20px; margin-left:auto; margin-right:auto; display:block; align:center;" />
                <h2>Booking Confirmed</h2>
                <p> Hi {{first_name}} {{last_name}}! The following are the details of your booking:</p>
                <table class="pure-table pure-table-bordered pure-table-striped">
                    <tbody>
                        <tr class="pure-table-odd">
                            <td><strong>Name</strong></td>
                            <td>{{first_name}} {{last_name}}</td>
                        </td>
                        <tr class="pure-table-odd">
                            <td><strong>Email</strong></td>
                            <td>{{email}}</td>
                        </td>
                        <tr class="pure-table-odd">
                            <td><strong>Timeslot</strong></td>
                            <td>{{timeslot[0]}} @ {{timeslot[1]}}hrs</td>
                        </td>
                    </tbody>
                </table>

                %if flag:
                <h2>{{flag}}</h2>
                %end
            </div>
        </div>
    </body>
</html>
