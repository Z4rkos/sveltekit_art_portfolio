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
    @tailwind base;
    @tailwind components;
    @tailwind utilities;

    .container {
        margin: 0 auto;
        text-align: center;
        height: 100%;
        position: relative;
    }

    .content {
        padding-bottom: 15px;
    }
</style>