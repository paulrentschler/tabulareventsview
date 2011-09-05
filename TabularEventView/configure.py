<configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:browser="http://namespaces.zope.org/browser"
    xmlns:five="http://namespaces.zope.org/five"
    xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
    xmlns:i18n="http://namespaces.zope.org/i18n"
    i18n_domain="TabularEventView">

    <five:registerPackage package="." initialize=".initialize" />

    <!-- Profiles -->
    <genericsetup:registerProfile
        name="default"
        title="Tabular Event View"
        directory="profiles/default"
        description="Tabular view of events in folders and collections."
        provides="Products.GenericSetup.interfaces.EXTENSION" />

    <!-- Views -->        
    <browser:page
        for="Products.ATContentTypes.interface.IATFolder"
        name="tabularevents_view"
        class=".views.TabularEventView"
        layer=".interfaces.ITabularEventView"
        template="templates/tabularevents_view.pt"
        permission="zope2.View"
    />

    <browser:page
        for="Products.ATContentTypes.interface.IATTopic"
        name="tabularevents_view"
        class=".views.TabularEventView"
        layer=".interfaces.ITabularEventView"
        template="templates/tabularevents_view.pt"
        permission="zope2.View"
    />

    <include package="plone.app.contentmenu"/>

    <browser:menuItem
        for="Products.ATContentTypes.interface.IATFolder"
        menu="plone_displayviews"
        layer=".interfaces.ITabularEventView"
        title="Tabular Events View"
        action="@@tabularevents_view"
        description="A view of events in tabular format"
    />
    
    <browser:menuItem
        for="Products.ATContentTypes.interface.IATTopic"
        menu="plone_displayviews"
        layer=".interfaces.ITabularEventView"
        title="Tabular Events View"
        action="@@tabularevents_view"
        description="A view of events in tabular format"
    />    

</configure>
