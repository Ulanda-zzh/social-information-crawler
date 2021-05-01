<template>
	<view>
		<view class="flex justify-between content0">
			设置
		</view>
		<!--头像开始--> 
		<view class="bg-white touxiang">
			<view style="display: flex;align-items: center;">
				<image style="width: 150upx;height: 150upx;"src="../../static/tab/touxiang.png"></image>
			</view>		
				<view class="denglu">
					<navigator url="../login/login">登录或注册</navigator>
				</view>
		</view>
		<!--头像结束-->
		<!--
		<view style="margin-top: 5upx;" class="flex justify-between align-center">
			<view class=""></view>
		</view>
		-->
		<!--列表部分-->
		<view class="list-content">
			<!--每一个列表项-->
			<view @tap="gopage(i)" class="bg-white list-item" v-for="(p,i) in lists":key="i">
				<text style="font-size: 170%;margin-right:10upx;" :class="p.icon"></text>
				<text>{{p.text}}</text>
			    <text style="font-size: 150%;margin-inline-start: 420upx;" :class="p.icon1"></text>
				</view>    
			</view>
			
			
			<!--每一个列表项-->
		</view>
		<!--列表部分-->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				denglu:[
					{
						url:"../login/login",
						}
				],
				
				lists:[
					{
						text:"外观设置",
						icon:"cuIcon-pic",
						icon1:"cuIcon-roundright"
					},
					{
						text:"帮助提醒",
						icon:"cuIcon-question",
						icon1:"cuIcon-roundright"
					},
					{
						text:"关联应用",
						icon:"cuIcon-link",
						icon1:"cuIcon-roundright"
					},
					{
						text:"通用指南",
						icon:"cuIcon-form",
						icon1:"cuIcon-roundright"
					},
					{
						text:"反馈意见",
						icon:"cuIcon-comment",
						icon1:"cuIcon-roundright"
					},
					{
						text:"关于我们",
						icon:"cuIcon-infofill",
						icon1:"cuIcon-roundright",
						
					},
					{
						text:"更多设置",
						icon:"cuIcon-add",
						icon1:"cuIcon-roundright"
					},
				]
				
			}
		},
		methods: {
			
		}		
	}
</script>

<style>
	.touxiang{
		height: 200upx;
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		align-items: center;
	}
	.padding{
		padding-left: 20upx;
	}
	
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
	.line{
		height: 1upx;
		background-color: #333333;
		flex-grow: 1;
	}
	.list-item{
		height: 115upx;
		display: flex;
		align-items: center;
		padding-left: 40upx;
		padding-right: 20upx;
		border-bottom: 1upx #DDDDDD solid;
	}
	.list-content{
		margin-top: 15upx;
		font-size: 120%;
	}
	.denglu{
		
		font-weight: bold;
		font-size: 150%;
	    color: #333333
		
	}
	
			
	
</style>
