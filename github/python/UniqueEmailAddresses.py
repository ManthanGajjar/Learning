class Solution(object):
    def numUniqueEmails(self, emails):
        uniqueEmailLen = 0
        emailObj = {}
        for listOfEmails in emails:
            splitVal = listOfEmails.split("@")[0].split("+")[0].replace(".", "") + "@" + listOfEmails.split("@")[1];
            emailObj[splitVal] = uniqueEmailLen;
            uniqueEmailLen += 1;
        return len(emailObj);
