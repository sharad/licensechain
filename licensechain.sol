// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LicenseChain {
    struct Resource {
        address[] owners;
        uint256 mintPrice;
        bool exists;
    }

    mapping(string => Resource) public resources; // resourceID => data

    event Minted(string resourceId, address owner, uint256 price);
    event Transferred(string resourceId, address from, address to, uint256 price);

    function mint(string memory resourceId, uint256 price) public payable {
        require(!resources[resourceId].exists, "Already minted");
        require(msg.value == price, "Incorrect minting cost");

        resources[resourceId].owners.push(msg.sender);
        resources[resourceId].mintPrice = price;
        resources[resourceId].exists = true;

        emit Minted(resourceId, msg.sender, price);
    }

    function sell(string memory resourceId, address to, uint256 price) public {
        require(resources[resourceId].exists, "Resource not found");

        bool isOwner = false;
        for (uint i = 0; i < resources[resourceId].owners.length; i++) {
            if (resources[resourceId].owners[i] == msg.sender) {
                isOwner = true;
                break;
            }
        }
        require(isOwner, "Not an owner");

        require(msg.sender != to, "Can't sell to self");
        require(price > 0, "Price must be > 0");

        // simulate transfer by recording ownership; real value transfer must be done off-chain or with ERC20
        resources[resourceId].owners.push(to);

        emit Transferred(resourceId, msg.sender, to, price);
    }

    function getOwners(string memory resourceId) public view returns (address[] memory) {
        return resources[resourceId].owners;
    }
}
