<template>
	<view class="content">
		
		<lxCalendar @change="change"></lxCalendar>
	</view>
</template>

<script>
	import lxCalendar from'../../components/lx-calendar/lx-calendar.vue'
	export default {
		components:{
			lxCalendar,
		},
		data() {
			return {
				title: 'Hello'
			}
		},
		onLoad() {

		},
		methods: {
			change(e){
				console.log(e);
			}

		}
	}
</script>

<style>

</style>
