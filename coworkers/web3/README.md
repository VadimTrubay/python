_WEB3 Project_
**Resources**

-   Applications https://cosmos.network/ecosystem/apps
-   Install Go, Rust

_Steps_

1. Launch new blockchain and set self validator
[Video](https://youtu.be/qzUgh8mvyJE)

Launch new blockchain

```
git clone https://github.com/cosmos/cosmos-sdk
```

```
 cd cosmos-sdk
```

```
git checkout tags/v0.44.3
```

```
make build
```

`cd build`

`./simd init project_name`

`./simd keys add name`

> we get next:

-   name: vlad
    type: local
    address: cosmos12hgu6sp4wxc773qkr4w0djedwgyx77annsp0ha
    pubkey: '{"@type":"/cosmos.crypto.secp256k1.PubKey","key":"Aowmkzc6Xpgn+nqqfl6Eg9C9OtSTLL0yKn69UASMYUbD"}'
    mnemonic: ""
    farm cancel inspire tomato have fever void cereal rain worry birth cat replace amused explain permit elegant moon gaze offer huge excuse follow potato

Make yourself a proper validator:

`./simd add-genesis-account vlad 100000000stake`

`./simd gentx vlad 70000000stake --chain-id test-chain-2M4ImQ`

`./simd collect-gentxs`

`./simd start`

Our blockchain was started, don't close terminal!

Open new terminal:

`cd cosmos-sdk/build`

Cheack balance

`./simd query bank balances $(./simd keys show name -a)`

Create new user

`./simd keys add student`

Send tokens to student
```
./simd tx bank send $(./simd keys show name -a) $(./simd keys show student -a) 10stake --chain-id test-chain-2M4ImQ
```

2. Use Ignite CLI
   [video](https://youtu.be/MTUQQ6nOkZo)

Install Ingite
```
curl https://get.ignite.com/cli! | bash
```

`cd checkers`

`ignite chain serve`

