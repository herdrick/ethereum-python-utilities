pragma solidity ^0.8.5;


contract TypesDemo {
  function bytesToAddress(bytes memory bys) private pure returns (address addr) {
    assembly {
        addr := mload(add(bys,20))
    }
  }


  bool public _isComplete = false;
  int public _int;
  string public _string;
  address public _address;
  bytes public _bytes;
  // bytes public a_bytes = ;

  function constantBool1() public view returns (bool) {
    return true;
  }

  function boolIdentity(bool x) public view returns (bool) {
    return x;
  }

  function markComplete() public {
    _isComplete = true;
  }

  function markNotComplete() public {
    _isComplete = false;
  }

  function getComplete() public returns (bool) {
    return _isComplete;
  }

  function setComplete(bool complete) public {
    _isComplete = complete;
  }

  function getCompleteView() public view returns (bool) {
    //console.log(".. calling getCompletionStatusView() now..");
    return _isComplete;
  }

  function getCompleteXor(bool x) public view returns (bool) {
    //console.log(".. calling getCompletionStatusView() now..");
    return _isComplete != x;
  }





  function constantInt1() public view returns (int) {
    return 123456;
  }

  function intIdentity(int x) public view returns (int) {
    return x;
  }

  function getInt() public returns (int) {
    return _int;
  }

  function setInt(int n) public {
    _int = n;
  }





  function constantString1() public view returns (string memory) {
    return "this is a string";
  }

  function stringIdentity(string memory x) public view returns (string memory) {
    return x;
  }

  function getString() public view returns (string memory) {
    return _string;
  }

  function setString(string memory s) public {
    _string = s;
  }




  function chooseString(string memory a, string memory b) public view returns (string memory) {
    return _isComplete ? a : b;
  }





  function constantAddress1() public view returns (address) {
    return address(0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87);    //"0x314159265C";
  }

  function constantAddress2() public view returns (address) {
    //return address("0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87");    //"0x314159265C";
    bytes memory foo = "0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87"; // this
    return bytesToAddress(foo);    //"0x314159265C";

  }

  function addressIdentity(address a) public view returns (address) {
    return a;
  }

  function getAddress() public view returns (address) {
    return _address;
  }

  function setAddress(address a) public {
    _address = a;
  }



  function constantBytes1() public view returns (bytes memory) {
    bytes memory foo = "0x01020304" ;
    return foo;    //"0x314159265C";
  }

  function constantBytes2() public view returns (bytes memory) {
    bytes memory foo = bytes("0x01020304");
    return foo;   //"0xf149c02b892556eC1fCf39bF43A3bF5B4A9F2346");    //"0x314159265C";
  }

  function bytesIdentity(bytes memory a) public view returns (bytes memory) {
    return a;
  }

  function getBytes() public view returns (bytes memory) {
    return _bytes;
  }

  function setBytes(bytes memory b) public {
    _bytes = b;
  }

}
