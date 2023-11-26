from zeep import Client

# Define the SOAP service URL
soap_url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'

# Create a SOAP client
client = Client(soap_url)

# Make a SOAP request to get information about a specific country (e.g., United States)
response = client.service.FullCountryInfo('USA')

# Print the response
print(response)
