# Basic Sample Hardhat Project

This project demonstrates a basic Hardhat use case. It comes with a sample contract, a test for that contract, a sample script that deploys that contract, and an example of a task implementation, which simply lists the available accounts.

Try running some of the following tasks:

```shell
npx hardhat accounts
npx hardhat compile
npx hardhat clean
npx hardhat test
npx hardhat node
node scripts/sample-script.js
npx hardhat help
```
[Site with Web3 app](https://waveportal-starter-project.vlad-bb.repl.co/)

[Replit](https://replit.com/@vlad-bb/waveportal-starter-project?v=1)

Remeber!
If you change contract code 
- You can Deploy new contract
```
npx hardhat run scripts/deploy.js --network rinkeby
```
- Get Contract addy (like that 0x5FbDB2315678afecb367f032d93F642f64180aa3) and change in your web3 app (app.js)
- Get data in artefacts/contracts/file.json, and write this data in web3 utils/file.json
