<template>
	<view>
		<view style="height: 200upx;"></view>
		<!--logo部分-->
		<view class="flex flex-direction align-center">
			<image class="logo" src="../../static/logo.png"></image>
			<view style="margin-top: 20upx;color: grey;">为你提供最好的时间管理</view>
		</view>
		<!--logo部分-->
		<!--输入部分-->
		<view style="margin-top: 20upx;">
			<view class="input-fa">
				<input class="log-input" placeholder="用户名/邮箱/手机号" v-model="form.phone" />
			</view>
			<view class="input-fa">
				<input class="log-input" :placeholder="status==0?'请输入密码':'请输入验证码'" v-model="form.password" :password="true"/>
				<button v-if="status==1">获取验证码</button>
			</view>
		</view>
		<!--输入部分-->
        <!--登录按钮-->
		<view style="flex justify-center margin-top: 50upx;" class="button">
			<navigator url="../my/my">
			<button @tap="login" class="bg-black round" style="width: 650upx;">
			   登录
			</button>
			</navigator>
		</view>
		<!--登录按钮-->
		<!--忘记密码 and 注册-->
		<view class="flex justify-between input-fa" style="margin-top: 10upx;">
			<text>忘记密码?</text>
			<text>新用户注册</text>
		</view>
		<!--忘记密码 and 注册-->
		<!--分割线-->
		<view style="margin-top: 80upx;" class="flex justify-between align-center">
			<view class="line"></view>
			<view style="color:gray">其他登录方式</view>
			<view class="line"></view>
		</view>
		<!--分割线-->
		<!--两个快捷登录的按钮-->
		<view class="flex justify-around" style="margin-top: 40upx;">
			<view class="flex flex-direction align-center justify-center">
				<image class="button-logo1" src="../../static/tab/Wechat.png"></image>
				<view>微信登录</view>
			</view>
			<view @tap="changestatus" class="flex flex-direction align-center justify-center">
				<image class="button-logo2" :src="status==0?'../../static/tab/phone.png':'../../static/tab/password.png'" style="margin-bottom: 10upx;margin-top: 10upx;"></image>
				<view>{{status==0?'验证码':'密码'}}登录</view>
			</view>
		</view>
		<!--两个快捷登录的按钮-->
		<!--固定的版权声明-->
		<view class="banquan" style="position: fixed;bottom: 10upx;color: grey;text-align: center;width: 750upx;">
			北京邮电大学 技术支持
			<br>
			登录代表您已同意<text class="text-blue">【隐私政策】</text>
		</view>
		<!--固定的版权声明-->

	</view>
</template>

<script>
	export default {
		data() {
			return {
				status:0,
				form:{
					phone:"",
					password:""
				}
			}
		},
		methods: {
			changestatus(){
				this.status=this.status===0?1:0;
			},
			login(){
				uni.request({
					url:"http://localhost/user/login",
					data:{
						phone:this.form.phone,
						password:this.form.password
					},
					method:"POST",
					success:(res)=>{
						uni.showToast({
							icon:"none",
							title:res.data.desc,
							//+(res.data.status==0?(','+res.data.info.name):'')
						})
						console.log(res.data);
						if(res.data.status!=0){
							//uni.setStorageSync("id",res.data.id);
							uni.switchTab({
								url:"../my/my"
							})
						}
					}
				})
			}
		}
	}
</script>

<style>
    .logo{
		width: 200upx;
		height: 200upx;
		
	}
	.log-input{
		height: 130upx;
		border-bottom: 1upx solid #DDDDDD ;
	}
	.input-fa{
		
		padding-left: 40upx;
		padding-right: 40upx;
		padding-bottom: 10upx;
	}
	.line{
		height: 1upx;
		background-color: #DDDDDD;
		flex-grow: 1;
	}
	
	.button-logo1{
		width: 75upx;
		height: 70upx;
	}
	.button-logo2{
		width: 50upx;
		height: 50upx;
	}
	.banquan{
		font-size: 80%;
	}
</style>
