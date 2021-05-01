<template>
	<view>
		<!--title-->
		<view class="flex content0">
				备忘录
		</view>
		<!--title-->
		<!--正文-->
		<view style="margin-top: 50upx;">
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			<view class="input-fa" style="display: flex;justify-content: space-around;align-items: center;">
				<image class="icon" style="width: 50upx;height: 50upx;" src="../../static/tab/more.png"></image>
				<input class="log-input" v-model="form.input1" />
				<image style="width: 50upx;height: 50upx;" src="../../static/tab/fdi.png"></image>
			</view>
			
			
			
		</view>
		<!--正文-->
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				form:{
					input1:"",
					input2:""
				}
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.content0{
		width: 750upx;
		height: 100upx;
		color: white;
		font-size: 150%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		font-weight: bold;
		background-color: #333333;
		}
    .input-fa{
		
		padding-left: 40upx;
		padding-right: 40upx;
		padding-bottom: 10upx;
	}
	.log-input{
		height: 90upx;
		border-bottom: 1upx solid #DDDDDD ;
	}
	.icon{
		color: black;
	}
</style>
