from abinator import (
    Abi,
    Event,
    Struct,
    indexed,
    payable,
    view,
    int24,
    uint24,
    uint96,
    uint128,
    uint256,
    address,
)


# part of https://github.com/Uniswap/v3-periphery/blob/main/contracts/interfaces/INonfungiblePositionManager.sol


class NonfungiblePositionManager(Abi):
    class IncreaseLiquidity(Event):
        tokenId: indexed(uint256)
        liquidity: uint128
        amount0: uint256
        amount1: uint256

    class DecreaseLiquidity(Event):
        tokenId: indexed(uint256)
        liquidity: uint128
        amount0: uint256
        amount1: uint256

    class Collect(Event):
        tokenId: indexed(uint256)
        recipient: address
        amount0: uint256
        amount1: uint256

    @view
    def positions(
        tokenId: uint256,
    ) -> tuple[
        uint96,
        address,
        address,
        address,
        uint24,
        int24,
        int24,
        uint128,
        uint256,
        uint256,
        uint128,
        uint128,
    ]:
        ...

    class MintParams(Struct):
        token0: address
        token1: address
        fee: uint24
        tickLower: int24
        tickUpper: int24
        amount0Desired: uint256
        amount1Desired: uint256
        amount0Min: uint256
        amount1Min: uint256
        recipient: address
        deadline: uint256

    @payable
    def mint(params: MintParams) -> tuple[uint256, uint128, uint256, uint256]:
        ...

    class IncreaseLiquidityParams(Struct):
        tokenId: uint256
        amount0Desired: uint256
        amount1Desired: uint256
        amount0Min: uint256
        amount1Min: uint256
        deadline: uint256

    @payable
    def increaseLiquidity(
        params: IncreaseLiquidityParams,
    ) -> tuple[uint128, uint256, uint256]:
        ...


NonfungiblePositionManager.to_abi()
