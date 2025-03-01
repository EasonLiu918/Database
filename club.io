<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36" version="24.7.17">
  <diagram id="R2lEEEUBdFMjLlhIrx00" name="Page-1">
    <mxGraphModel dx="2600" dy="928" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" value="Members" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#dae8fc;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;strokeColor=#6c8ebf;" parent="1" vertex="1">
          <mxGeometry x="200" y="750" width="160" height="234" as="geometry" />
        </mxCell>
        <mxCell id="3" value="+ members_id (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="2" vertex="1">
          <mxGeometry y="26" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="4" value="+ members_name" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="2" vertex="1">
          <mxGeometry y="52" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="5" value="+ members_date_of_birth" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="2" vertex="1">
          <mxGeometry y="78" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="6" value="+ members_phone_number" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="2" vertex="1">
          <mxGeometry y="104" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="7" value="+ members_gender" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="2" vertex="1">
          <mxGeometry y="130" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="8" value="+ members_email" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="2" vertex="1">
          <mxGeometry y="156" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="9" value="+ members_preferences" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="2" vertex="1">
          <mxGeometry y="182" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="10" value="+ membership_type_id (FK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="2" vertex="1">
          <mxGeometry y="208" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="11" value="Location" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#d5e8d4;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;strokeColor=#82b366;" parent="1" vertex="1">
          <mxGeometry x="420" y="610" width="160" height="130" as="geometry" />
        </mxCell>
        <mxCell id="12" value="+ location_id (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="11" vertex="1">
          <mxGeometry y="26" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="13" value="+ capacity" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="11" vertex="1">
          <mxGeometry y="52" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="14" value="+ type" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="11" vertex="1">
          <mxGeometry y="78" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="15" value="+ availability" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="11" vertex="1">
          <mxGeometry y="104" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="16" value="Activity" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#fff2cc;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;strokeColor=#d6b656;" parent="1" vertex="1">
          <mxGeometry x="609" y="270" width="160" height="182" as="geometry" />
        </mxCell>
        <mxCell id="17" value="+ activity_id (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="16" vertex="1">
          <mxGeometry y="26" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="18" value="+ activity_name" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="16" vertex="1">
          <mxGeometry y="52" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="19" value="+ description" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="16" vertex="1">
          <mxGeometry y="78" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="20" value="+ activity_status" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="16" vertex="1">
          <mxGeometry y="104" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="21" value="+ participation_quota" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="16" vertex="1">
          <mxGeometry y="130" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="22" value="+ location_id (FK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="16" vertex="1">
          <mxGeometry y="156" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="23" value="Signup" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#f8cecc;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;strokeColor=#b85450;" parent="1" vertex="1">
          <mxGeometry x="161" y="216" width="160" height="156" as="geometry" />
        </mxCell>
        <mxCell id="24" value="+ signup_id (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="23" vertex="1">
          <mxGeometry y="26" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="25" value="+ members_id (FK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="23" vertex="1">
          <mxGeometry y="52" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="26" value="+ activity_id (FK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="23" vertex="1">
          <mxGeometry y="78" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="27" value="+ signup_date" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="23" vertex="1">
          <mxGeometry y="104" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="28" value="+ signup_time" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="23" vertex="1">
          <mxGeometry y="130" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="29" value="Feedback" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;strokeColor=#9673a6;" parent="1" vertex="1">
          <mxGeometry x="420" y="870" width="160" height="182" as="geometry" />
        </mxCell>
        <mxCell id="30" value="+ feedback_id (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="29" vertex="1">
          <mxGeometry y="26" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="31" value="+ activity_id (FK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="29" vertex="1">
          <mxGeometry y="52" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="32" value="+ members_id (FK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="29" vertex="1">
          <mxGeometry y="78" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="33" value="+ rating" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="29" vertex="1">
          <mxGeometry y="104" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="34" value="+ comments" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="29" vertex="1">
          <mxGeometry y="130" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="35" value="+ feedback_date" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="29" vertex="1">
          <mxGeometry y="156" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="36" value="MembershipType" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#ffe6cc;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;strokeColor=#d79b00;" parent="1" vertex="1">
          <mxGeometry x="-20" y="720" width="160" height="130" as="geometry" />
        </mxCell>
        <mxCell id="37" value="+ membership_type_id (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="36" vertex="1">
          <mxGeometry y="26" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="38" value="+ type_name" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="36" vertex="1">
          <mxGeometry y="52" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="39" value="+ description" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="36" vertex="1">
          <mxGeometry y="78" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="40" value="+ fee" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="36" vertex="1">
          <mxGeometry y="104" width="160" height="26" as="geometry" />
        </mxCell>
        <mxCell id="41" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERoneToMany;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="37" target="10" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="370" y="360" as="sourcePoint" />
            <mxPoint x="470" y="260" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="42" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERoneToMany;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="12" target="22" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="370" y="360" as="sourcePoint" />
            <mxPoint x="470" y="260" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="44" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERoneToMany;rounded=0;" parent="1" source="17" target="26" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="370" y="360" as="sourcePoint" />
            <mxPoint x="470" y="260" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="45" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERoneToMany;rounded=0;" parent="1" target="31" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="770" y="310" as="sourcePoint" />
            <mxPoint x="470" y="260" as="targetPoint" />
            <Array as="points">
              <mxPoint x="820" y="620" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="46" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERoneToMany;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" target="32" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="360" y="789" as="sourcePoint" />
            <mxPoint x="470" y="260" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wYa22XWhmUOGpcuybt-T-47" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERoneToMany;rounded=0;" edge="1" parent="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="360" y="789" as="sourcePoint" />
            <mxPoint x="160" y="280" as="targetPoint" />
            <Array as="points">
              <mxPoint x="260" y="650" />
            </Array>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
