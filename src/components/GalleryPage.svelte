<script>
    export let imagePaths;
</script>  


{#each imagePaths as image}
<img src={image} alt="">
{/each}


<style>
    img {
        margin: auto;
        padding-bottom: 50px;
    }
</style>