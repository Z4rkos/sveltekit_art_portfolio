
<script>
function fade(node, {
	delay = 0,
	duration = 200
}) {
	const o = +getComputedStyle(node).opacity;

	return {
		delay,
		duration,
		css: t => `opacity: ${t * o}`
	};
}
</script>