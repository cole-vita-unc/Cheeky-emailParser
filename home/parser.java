// address object
public class Address{
    int address;
    String street;
    int aptNum;
    int zip;
    String city;
    String state;
    String country;

    public Address(int address, String street, int aptNum, int zip, String city, String state, String country){
        this.address = address;
        this.street = street;
        this.zip = zip;
        this.city = city;
        this.state = state;
        this.country = country;
    }
}

// function returns address