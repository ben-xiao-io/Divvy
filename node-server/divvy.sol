pragma solidity >=0.4.25 <0.6.0;

contract Divvy {
  address public creator;
  mapping (address => uint) public balances;
  
  //the event that notifies when a transfer is complete
  event Delivered(address from, address to, uint amount);
  
  function DivvyCoin() public {
      creator = msg.sender;
  }
  
  function create(address receiver, uint amount) public {
      if(msg.sender != creator) revert();
      balances[receiver] += amount;
  }
  
  function transfer(address receiver, uint amount) public {
      if (balances[msg.sender] < amount) revert();
      balances[msg.sender] -= amount;
      balances[receiver] += amount;
      emit Delivered(msg.sender, receiver, amount);
  }
}