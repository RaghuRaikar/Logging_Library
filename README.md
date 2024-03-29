# Logging Library

A python program that can be run on files to search for personal information and replace it if found while also sending out an alert email.


# Company Scenario

 - You are working for Amazon and are part of their returns department.
 - Contain logs of all their customer returns containing personal information about the customer and the details of their return.
 - Log has been scrubbed for the most part but needs to be double checked to be certain.
 - Run a script that makes sure the log files have no sort of personal information.

## Personal Information Being Searched For

 - First and Last Name
 - Address
 - Phone Number
 - Email
 - Social Security

## How The Program Works

 - Uses python regular expressions library in order to be able to identify personal information.
 - Parses file in search of personal information and replaces it with word “<REDACTED'>”.
 - Sends an email out to the Amazon Returns team letting them know that personal information was found and thus the current data in the log file could have been subject to a data breach.
 - Includes the order IDs of the specific orders that contained personal information in case the team wants to go back and identify all the customer’s personal information that was at risk.


## Email Layout

Dear Amazon Returns Team,

This email is being sent out in order to notify you that personal information was found, and thus might have been subject to a data breach. This personal information was redacted and the file was updated.

Here is a list of all the Order IDs which contained Personal Information:

Order ID: {order_list}

Thank you.

## Future Use Cases Of This Program

 - Can be used to scan any sort of file for personal information.
 - Uses Regular Expressions so it is able to find personal information regardless of how the file is formatted.
 - Good way of alerting people through email if a file contains personal information.
 - Keeps personal data secure.
