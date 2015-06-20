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
                <h2>What is Cyberdelia?</h2>
                <p>Cyberdelia is a club that was built from scratch in an abandoned indoor swimming pool on the outskirts of London, with its center in the depths of what was the pool. It is a place where hackers can meet up, hang out, exchange information, brag about hacks, and best each other in video games. We have a multi-leveled layout with ramps for those on rollerblades and stairs for all the foot-walking lamerz. We invite all l33t h4ck3ers (except "The Plague" who still has an unpaid bar tab of ~$100000) from all walks of life to hang out at our premises. Make your reservations below!</p>
            </div>

            <div class="pure-u-1 pure-u-md-1-3">

                <form action="/booking" method="post" class="pure-form">
                    <h2>Personal Details</h2>
                    <fieldset class="pure-group">
                        <input name="first_name" type="text" class="pure-input-1-2" placeholder="First Name" required>
                        <input name="last_name" type="text" class="pure-input-1-2" placeholder="Last Name" required>
                        <input name="email" type="email" class="pure-input-1-2" placeholder="Email" required>
                    </fieldset>

                    <h2>Available Timeslots</h2>
                    <p>All bookings should be done a day in advance. If you're late, too bad.</p>

                    <fieldset class="pure-group">
                       <table class="pure-table pure-table-bordered pure-table-striped" width="50%">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Date</th>
                                    <th>Time</th>
                                    <th></th>
                                </tr>
                            </thead>

                            <tbody>
                                %for index, slot in enumerate(timeslots):
                                <tr class="pure-table-odd">
                                    <td>{{index+1}}</td>
                                    <td>{{slot[0]}}</td>
                                    <td>{{slot[1]}}</td>
                                    <td>
                                        <label for="timeslot" class="pure-radio">
                                            <input name="timeslot" type="radio" value={{slot[2]}}>
                                        </label>
                                    </td>
                                </tr>
                                %end
                            </tbody>
                        </table>
                    </fieldset>

                    <button type="submit" class="pure-button pure-input-1-2 pure-button-primary">Submit</button>
                </form>
            </div>
        </div>
    </body>
</html>
