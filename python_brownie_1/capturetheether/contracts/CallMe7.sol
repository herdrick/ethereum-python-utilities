pragma solidity ^0.8.5;

contract CallMe7 {
  bool public _isComplete = false;

  function getCompletionStatusPublic() public returns (bool) {
    return _isComplete;
  }

  function getCompletionStatusView() public view returns (bool) {
    //console.log(".. calling getCompletionStatusView() now..");
    return _isComplete;
  }

  function markComplete() public {
    _isComplete = true;
  }

  function markNotComplete() public {
    _isComplete = false;
  }


}
