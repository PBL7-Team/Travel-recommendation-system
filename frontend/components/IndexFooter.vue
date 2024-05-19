<template>
    <section class="footer-dark">
        <div class="container-15">
            <div class="footer-wrapper">
                <div class="footer-left-wrapper"><a href="#" class="navbar-logo-link-2 w-nav-brand"><img
                            src="@/assets/images/team_logo1.png"
                            loading="lazy" sizes="140px"
                            alt="Logo"></a>
                    <div class="spacer-m"></div>
                    <div>The Smarter Way to Travel</div>
                    <div class="spacer-l"></div>
                </div>
                <div class="footer-content">
                    <div class="footer-block">
                        <div class="title-small">EXPLORE</div>
                        <a href="/chatbot" class="footer-link">Chatbot</a>
                        <a href="/itinerary-planner" class="footer-link">Itinerary Builder</a>
                        <a href="/thematic-advisors" class="footer-link">Thematic Advisors</a>
                        <a href="/destinations" class="footer-link">Destination Guides</a>
                    </div>
                    <div class="footer-block">
                        <div class="title-small">Company</div><a href="/about" class="footer-link">About Us</a><a
                            href="/blog" class="footer-link">Travel Blog</a><a href="/contact"
                            class="footer-link">Partnerships</a><a href="mailto:press@usevacay.com"
                            class="footer-link">Press &amp; Media</a>
                    </div>
                    <div class="footer-block">
                        <div class="title-small">Useful Links</div><a href="/user-profile" data-ms-content="!members"
                            class="footer-link">Log In</a><a href="/contact" class="footer-link">Support</a><a
                            href="/pricing" class="footer-link">Pricing</a><a href="/feedback"
                            class="footer-link">Feedback</a>
                    </div>
                </div>
            </div>
            <div class="uui-footer08_bottom-wrapper-2">
                <div class="uui-text-size-small-18 text-color-gray500">© 2024 Bold Voyage Heros, Inc.</div>
                <div class="w-layout-grid uui-footer08_legal-list-2"><a href="/terms-of-service"
                        class="uui-footer08_legal-link-2">Terms of Service</a><a href="/privacy-policy"
                        class="uui-footer08_legal-link-2">Privacy Policy</a></div>
            </div>
        </div>
    </section>
</template>

<script setup>

</script>
<style lang="scss" scoped>
.footer-dark {
    background-color: #f5f7fa;
    border-bottom: 1px solid #e4ebf3;
    padding: 50px 30px 15px;
    position: relative;
}

.container-15 {
    width: 100%;
    max-width: 940px;
    margin-left: auto;
    margin-right: auto;
}

@media screen and (max-width: 991px) {
    .container-15 {
        max-width: 728px;
    }
}

.footer-wrapper {
    justify-content: space-between;
    align-items: flex-start;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
}

.footer-left-wrapper {
    flex-direction: column;
    display: flex;
}

.navbar-logo-link-2 {
    max-width: 140px;
    padding-top: 5px;
    padding-left: 0;
}

.w-nav-brand {
    float: left;
    color: #333;
    text-decoration: none;
    position: relative;
}

.footer-content {
    grid-column-gap: 70px;
    grid-row-gap: 40px;
    grid-template: "." / auto auto 1fr;
    grid-auto-columns: .25fr;
    display: grid;
}

@media screen and (max-width: 991px) {
    .footer-content {
        grid-column-gap: 60px;
    }
}

.title-small {
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 12px;
    font-size: 14px;
    font-weight: 700;
    line-height: 16px;
}

.footer-block {
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
}

.footer-link {
    color: #1a1b1f;
    margin-top: 12px;
    margin-bottom: 6px;
    font-size: 13px;
    line-height: 16px;
    text-decoration: none;
}
</style>