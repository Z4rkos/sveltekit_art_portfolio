<script>
    import { fade } from "svelte/transition"
    export let columns = 3;
</script>


<div transition:fade="{{duration:160}}" class="container" style="grid-template-columns:repeat({columns}, auto);">
    <slot></slot>
</div>



<style>
    .container {
        box-sizing: border-box;
        width: 100%;
        display: grid;
        grid-row-gap: 35px;
        grid-column-gap: 60px;
        justify-content: center;
        align-items: flex-start;
    }


    @media(max-width: 750px) {
        .container {
            display: block;
        }   
    }
</style>
