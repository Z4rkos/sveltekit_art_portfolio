<script>
    import Header from "../components/layout/Header.svelte";
    import Footer from "../components/layout/Footer.svelte";

</script>


<div class="container">
    <Header />

    <div class="content">
        <slot></slot>
    </div>
    <Footer />
</div>


<style>
    @import "/static/global.css";
    @tailwind base;
    @tailwind components;
    @tailwind utilities;

    

    .container {
        width: 70%;
        margin: 0 auto;
        text-align: center;
        height: 100%;
        position: relative;
        font-family: Impact, Charcoal, sans-serif;
        

    }

    .content {
        padding-bottom: 15px;
    }

    @media(max-width: 750px) {
        .container {
            width: 80%;
        }
    }
</style>