<script>

</script>

<form action="">
    <div class="form-container">
        <h1>Contact Me:</h1>

        <div class="name-container">
            <div class="form-content">
                    <label for="fname">First Name*</label>
                <input type="text" name="fname">
            </div>

            <div class="form-content">
                <label for="lname">Last Name</label>
                <input type="text" name="lname">
            </div>
        </div>

        <div class="form-content">
            <label for="email">Email Addres*</label>
            <input type="text" name="email">
        </div>

        <div class="form-content">
            <label for="subject">Subject</label>
            <input type="text" name="subject">
        </div>

        <div class="form-content">   
            <label for="message">Message*</label>    
            <textarea name="message"></textarea>
        </div>

        <button class="">Submit</button>
    </div>

</form>

<style>

    h1 {
        font-size: 30px;
        font-weight: 300;
        margin-bottom: 20px;
        border-bottom: solid black;
        border-width: 15px;
    }

    button {
        height: 40px;
        width: 50%;
        background-color: black;
        color: white;
        align-self: center;
    }

    .form-container {
        display: flex;
        flex-direction: column;
        gap: 1.2rem;
        margin: 50px auto;
    }

    .name-container {
        display: flex;
        gap: 20px;
    }

    .form-content {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .form-content input, textarea {
        border: 1px solid rgb(197, 197, 197);
        width: 100%;
        height: 35px;
    }

    .form-content textarea {
        height: 200px
    }

    @media(min-width: 1100px) {
        .form-container {
            width: 80%;
        }
    }

    
</style>